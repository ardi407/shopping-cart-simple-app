class CartItem: 
    '''
    Class untuk membuat input user sebuah object ChartItem
    '''
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart: 
    '''
    Class yang memiliki 3 methods yaitu menambah, menghapus dan melihat barang dalam keranjang.
    '''
    def __init__(self): # Constructor class yang di dalamnya hanya terdapat attribure self.cart untuk container items
        self.cart = [] 

    
    def addItem(self, item, price):
        '''
        method untuk menambahkan barang dengan input nama item dan harga.
        '''
        new_item = CartItem(item, price) # membuat new item sebagai object class CartItem
        self.cart.append(new_item) # menambahkan setiap barang ke dalam container cart
        
    def displayItem(self): 
        '''
        method untuk menampilkan semua barang
        jika cart kosong maka tampilkan pesan Keranjang Kosong.
        jika cart tidak kosong, maka tampilkan isi keranjang.
        contoh:
        ----------------------------
        Isi Keranjang Anda:
        1. Baju ----- Rp. 10000.00
        2. Celana ----- Rp. 10000.00
        ----------------------------
        '''
        if len(self.cart) == 0: 
            print('Keranjang Kosong')  
        if len(self.cart) > 0:
            print("Isi Keranjang Anda:") 
            for index, entry in enumerate(self.cart): 
                # print output yang sudah diformat dengan numbering mulai dari 1, harga diubah menjadi string.
                print(str(index+1)+'. '+ entry.name +" ----- Rp. "+ str(entry.price)+".00") 

    def deleteItem(self, item): # method untuk menghapus barang
        '''
        method untuk menampilkan semua barang.
        jika cart kosong maka akan menampilkan pesan: >> Keranjang kosong, tidak menghapus apapun
        Jika cart tidak kosong, maka barang akan dicari.
        jika barang ditemukan, maka hapus penemuan pertama dari for loop sesuai dengan kata kunci.
        jika ada lebih dari satu barang dengan nama yang sama, barang yang paling atas akan dihapus terlebih dahulu (Harus diinput lagi jika ingin menghapus lagi).
        jika barang tidak ditemukan, maka tampilkan pesan: Barang dengan kata '{item}' tidak ditemukan!
        '''
        if len(self.cart) == 0: 
            print(f"\n>> Keranjang kosong, tidak menghapus apapun") 
            return(f"\n>> Keranjang kosong, tidak menghapus apapun") # Ini dibuat untuk unit testing
        else:
            item_found = False # Untuk menandakan jika barang ditemukan
            for entry in self.cart: 
                if entry.name == item: 
                    self.cart.remove(entry) # hapus entry dari container chart
                    print(f"\n>> '{item}' berhasil dihapus") 
                    item_found = True 
                    return(f"\n>> '{item}' berhasil dihapus") 
                
            # ketika barang tidak ditemukan, maka if conditional berlaku. Ketika barang sudah ditemukan, maka if tidak dijalankan
            if not item_found: 
                print(f"\n>> Barang dengan kata '{item}' tidak ditemukan!") 
                return(f"\n>> Barang dengan kata '{item}' tidak ditemukan!") # untuk keperluan unit testing

    def totalPrice(self): 
        '''
        method untuk menghitung total harga barang dalam keranjang.
        '''
        total_price = 0 
        for entry in self.cart: 
            total_price += entry.price 
        return total_price 
    
    def userInterface(self):
        '''
        method ini berguna untuk menampilkan user interface program.
        '''

        exit = False # untuk while loop interface 

        # Header toko
        print("===================-☀*☀_A_☀*☀-=====================\n")
        print("      Selamat Datang di Toko Serba Ada Sejahtera\n")
        print("====================================================\n")


        while not exit: #ketika exit masih false
            #tampilkan menu
            print('Menu:')
            print('1. Menambah Barang')
            print('2. Hapus Barang')
            print('3. Tampilkan Barang di Keranjang')
            print('4. Lihat Total Belanja')
            print('5. Exit')
            print('------------------------------------\n')
            
            # untuk membuat user input menu yang sesuai, while loop digunakan
            while True:
                try:
                    menuInput = int(input("Masukan pilihan anda(1-5): ")) #Jika diinput negative otomatis error karena '-' adalah string
                    if menuInput <=0 or menuInput > 5: #jika input lebih dari 5. 
                        raise ValueError #raise valueerror
                except:           
                    print(f"Oops, masukan hanya angka 1-5 ya") 
                else:
                    print(f"Pilihan anda: {menuInput}\n") 
                    break #break kondisi while loop jika input menu sudah benar
            # conditionals if untuk menu 1 - 5
            if menuInput == 1: 
                item=input('Masukan nama barang: ').strip() 
                
                while True: #special case untuk harga, harus diinput dengan integer. Jika tidak, input harga akan di prompt terus menerus
                    try:
                        price=int(input('Masukan harga barang: '))
                        print('--------------------------------------------------')
                        self.addItem(item,price)
                    except:
                        print("Opps, masukan angka pada harga ya!")
                        print('--------------------------------------------------')
                    else:
                        print(f"Barang '{item}' berhasil dimasukkan ke keranjang")
                        print('--------------------------------------------------\n')
                        break

            elif menuInput == 2: 
                print("----------------------------")
                self.deleteItem(item=input('Masukan barang yang akan dihapus: ').strip())
                print("----------------------------")
            elif menuInput == 3: 
                print('----------------------------')
                self.displayItem()
                print("----------------------------")
            elif menuInput == 4: 
                total = self.totalPrice()
                print("----------------------------")
                print(f"Total Harga: Rp. {total}.00")
                print("----------------------------")
            else: # menu 5 untuk keluar dari program. (Tidak secara explicit karena sudah diatur pada try-except di atas)
                print('Terimkasih sudah berbelanja di toko kami')
                print('Sampai berjumpa Kembali')
                print('===========================================')
                exit = True
            

if __name__ == "__main__":

    varCart = ShoppingCart() # assign chart ke dalam kelas ShoppingChart
    varCart.userInterface() # trigger user interface
