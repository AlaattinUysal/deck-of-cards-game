import tkinter as tk
from tkinter import messagebox
from deck_of_cards import Deck
from PIL import Image, ImageTk
import random

class CardGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kart Oyunu")

        # Arka plan resmi ayarlama
        self.background_image = Image.open("D:/CURSOR/SideProjects/Deck_of_cards/assets/wallpaper.jpg ")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Kalan Kartlar: 52", font=("Helvetica", 16), bg="lightgrey")
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text="Puan: 0", font=("Helvetica", 16), bg="lightgrey")
        self.score_label.pack(pady=10)

        self.computer_score_label = tk.Label(root, text="Bilgisayar Puanı: 0", font=("Arial", 16), bg="lightyellow", fg="darkred")
        self.computer_score_label.pack(pady=10)

        self.computer_hand_label = tk.Label(root, text="Bilgisayar Eldeki Kart Sayısı: 0", font=("Arial", 16), bg="lightyellow", fg="darkred")
        self.computer_hand_label.pack(pady=10)

        self.player_hand_label = tk.Label(root, text="Eldeki Kart Sayısı: 0", font=("Arial", 16), bg="lightgrey", fg="blue")
        self.player_hand_label.pack(pady=10)

        self.entry_label = tk.Label(root, text="Kaç kart çekmek istersiniz? (Max: 8)", font=("Helvetica", 14), bg="lightgrey")
        self.entry_label.pack(pady=10)

        self.card_count_entry = tk.Entry(root, font=("Helvetica", 14))
        self.card_count_entry.pack(pady=10)
        self.card_count_entry.bind("<Return>", self.draw_card)

        self.draw_button = tk.Button(root, text="Kart Çek", command=self.draw_card, font=("Helvetica", 14), bg="lightblue", fg="black", relief="raised", bd=3)
        self.draw_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Çık", command=self.exit_game, font=("Helvetica", 14), bg="red", fg="white", relief="raised", bd=3)
        self.quit_button.pack(pady=10)

        self.continue_button = tk.Button(root, text="Devam Et", command=self.continue_game, font=("Helvetica", 14), bg="gold", fg="black", relief="raised", bd=3)
        self.continue_button.pack(pady=(10, 50))  # Butonu biraz daha aşağı kaydır
        self.continue_button.pack_forget()  # Başlangıçta butonu gizle

        # Ayarlar butonu (sadece simge) - Sol üst köşeye yerleştirildi
        self.settings_button = tk.Button(root, text="⚙️", command=self.open_settings, font=("Helvetica", 14), bg="lightgrey", fg="black", relief="raised", bd=3)
        #self.settings_button.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)
        self.settings_button.place(x=5, y=5)
  # Tam sol üst köşeye yerleştir

        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []  # Oyuncunun elindeki kartlar
        self.computer_hand = []  # Bilgisayarın elindeki kartlar
        self.score = 0  # Oyuncunun puanı
        self.computer_score = 0  # Bilgisayarın puanı

        # Pencere boyutunu ayarlama
        self.root.geometry("800x600")  # Başlangıç boyutu
        self.root.bind("<Configure>", self.resize_background)  # Pencere boyutu değiştiğinde arka planı yeniden boyutlandır

        # Ayrım çizgisi
        self.divider = tk.Frame(root, width=2, bg="black")
        self.divider.pack(side=tk.LEFT, fill=tk.Y)

        # Kart çekme sınırı
        self.max_draw = 8

        # Çekilen kartları gösteren alan
        self.drawn_cards_label = tk.Label(root, text="Çekilen Kartlar:", font=("Helvetica", 14), bg="lightgrey")
        self.drawn_cards_label.pack(pady=10)

        self.drawn_cards_display = tk.Text(root, height=10, width=30, font=("Helvetica", 12), bg="white")
        self.drawn_cards_display.pack(pady=10)

    def resize_background(self, event):
        width = event.width
        height = event.height
        resized_image = self.background_image.resize((width, height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.background_label.config(image=self.background_photo)

    def calculate_score(self, cards):
        score = 0
        for card in cards:
            if card.value in ["J", "Q", "K"]:
                score += 10
            elif card.value == "A":
                score += 11
            elif card.value in ["2", "3", "4", "5", "6"]:  # Eksi puan veren kartlar
                score -= 6
            else:
                score += int(card.value)
        return score

    def draw_card(self, event=None):
        try:
            number = int(self.card_count_entry.get())
            if number <= 0 or number > self.max_draw:
                raise ValueError(f"1 ile {self.max_draw} arasında bir sayı girin.")
            if self.deck.count() >= number:
                cards = self.deck.deal_hand(number)
                self.player_hand.extend(cards)  # Çekilen kartları oyuncunun eline ekle
                self.label.config(text=f"Kalan Kartlar: {self.deck.count()}")
                self.player_hand_label.config(text=f"Eldeki Kart Sayısı: {len(self.player_hand)}")  # Elindeki kart sayısını güncelle
                
                self.score += self.calculate_score(cards)  # Oyuncunun puanını hesapla
                self.score_label.config(text=f"Puan: {self.score}")

                # Çekilen kartları göster
                self.drawn_cards_display.delete(1.0, tk.END)  # Önceki kartları temizle
                for card in cards:
                    card_score = self.calculate_score([card])
                    self.drawn_cards_display.insert(tk.END, f"Player: {card} ({card_score} puan)\n")

                # Kalan kart sayısını güncelle
                self.update_remaining_cards()

                # Oyun bitip bitmediğini kontrol et
                if self.deck.count() == 0:
                    self.show_winner()  # Oyun bittiğinde kazananı göster
                else:
                    # Bilgisayarın kart çekmesi
                    self.root.after(1000, self.computer_turn)  # 1 saniye bekle ve bilgisayarın sırasını başlat
            else:
                messagebox.showinfo("Oyun Bitti", "Yeterli kart yok!")
        except ValueError as e:
            messagebox.showerror("Hata", str(e))

    def update_remaining_cards(self):
        total_cards = 52 - (len(self.player_hand) + len(self.computer_hand))
        self.label.config(text=f"Kalan Kartlar: {total_cards}")

    def computer_turn(self):
        self.computer_hand_label.config(text="Bilgisayar kart çekiyor...")
        self.root.update()  # Arayüzü güncelle

        self.root.after(3000, self.perform_computer_draw)  # 3 saniye bekle

    def perform_computer_draw(self):
        computer_draw = random.randint(1, self.max_draw)  # Bilgisayar 1-8 kart çekebilir
        computer_cards = self.deck.deal_hand(computer_draw)
        self.computer_hand.extend(computer_cards)  # Bilgisayarın eline ekle
        self.computer_score += self.calculate_score(computer_cards)
        self.computer_score_label.config(text=f"Bilgisayar Puanı: {self.computer_score}")
        self.computer_hand_label.config(text=f"Bilgisayar Eldeki Kart Sayısı: {len(self.computer_hand)}")  # Toplam kart sayısını göster

        # Çekilen kartları göster
        self.drawn_cards_display.insert(tk.END, f"Computer: {', '.join(map(str, computer_cards))}\n")

        # Kalan kart sayısını güncelle
        self.update_remaining_cards()

        # Oyun bitip bitmediğini kontrol et
        if self.deck.count() == 0:
            self.show_winner()  # Oyun bittiğinde kazananı göster
        else:
            self.continue_button.pack()  # Devam et butonunu göster

    def show_winner(self):
        # Önceki kazanan mesajlarını temizle
        for widget in self.root.pack_slaves():
            if isinstance(widget, tk.Label) and widget.cget("font") == ("Helvetica", 24):
                widget.pack_forget()

        # Kazanan mesajını oluştur
        if self.score > self.computer_score:
            winner_text = "WINNER: Siz Kazandınız!"
        elif self.score < self.computer_score:
            winner_text = "GAME OVER: Bilgisayar Kazandı!"  # GAME OVER yazısı
        else:
            winner_text = "Beraberlik!"

        # Kazanan yazısının rengi değiştirildi
        winner_label = tk.Label(self.root, text=winner_text, font=("Helvetica", 24), bg="lightgrey", fg="darkblue")  # Arka planla uyumlu renk
        winner_label.pack(pady=20)

        # Oyun bitince devam et butonunu gizle
        self.continue_button.pack_forget()

    def continue_game(self):
        self.continue_button.pack_forget()  # Butonu gizle
        self.label.config(text="Devam ediliyor...")  # Kullanıcıya bilgi ver

    def exit_game(self):
        self.root.quit()  # Uygulamadan çık

    def open_settings(self):
        # Ayarlar penceresi açma
        
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Ayarlar")
        settings_window.geometry("300x200")

        # Ayarlar içeriği
        settings_label = tk.Label(settings_window, text="Ayarlar", font=("Helvetica", 16))
        settings_label.pack(pady=10)

        # Örnek ayar: Ses açma/kapama
        sound_var = tk.BooleanVar(value=True)
        sound_check = tk.Checkbutton(settings_window, text="Ses Açık", variable=sound_var)
        sound_check.pack(pady=10)

        # Kapat butonu
        close_button = tk.Button(settings_window, text="Kapat", command=settings_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CardGameApp(root)
    root.mainloop()
    