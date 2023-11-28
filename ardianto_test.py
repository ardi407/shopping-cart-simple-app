"""
=====================================================================================================
Graded Challenge 1

Nama        : Ardianto
Batch       : RM-024

Program ini dibuat untuk unit testing Aplikasi Shopping Chart
>>> berisikan unit testing untuk method addItem, deleteItem, dan totalPrice dalam class ShoppingChart
=====================================================================================================
"""


from ardianto_app import ShoppingCart  # import class ShoppingChart
import unittest # import Module tnittest

class TestShoopingCart(unittest.TestCase):
    '''
    class unit testing yang inherits class TestCase dari module unittest
    '''
    def setUp(self):
        '''
        # sebuah method untuk mengatur setUp, agak mirip dengan __init__
        '''
        # self.test_chart adalah nama atribut dalam class test
        self.test_cart = ShoppingCart()
    
    def test_addItem(self): 
        '''
        Test untuk method addItem / menambahkan barang
        self.test_chart.chart[0].name < 'name' adalah penamaan dalam class ChartItem
                  ^      ^    ^index
         container | attribute dalam class asli ShoppingChart
        '''
        # Tambahkan 2 barang Apel dan Anggur
        self.test_cart.addItem('Apel', 10000)
        self.test_cart.addItem('Anggur', 15000)
        
        # test apakah keranjang sama dengan 2 (sesuai dengan jumlah barang yang di masukan)
        self.assertEqual(len(self.test_cart.cart), 2, "Jumlah tidak sesuai")

        # test apakah barang dengan index 0 sama dengan Apel
        self.assertEqual(self.test_cart.cart[0].name, 'Apel') 

        # test apakah barang dengan index 1 sama dengan Anggur
        self.assertEqual(self.test_cart.cart[1].name, 'Anggur')

        # test apakah harga barang dengan index 0 sama dengan 10000 
        self.assertEqual(self.test_cart.cart[0].price, 10000)

        # test apakah harga barang dengan index 1 sama dengan 15000
        self.assertEqual(self.test_cart.cart[1].price, 15000) 
        
        

    def test_deleteItem(self):
        ''' 
        Test untuk Method deleteItem / menghapus barang
        '''
        #tambahkan dulu 2 barang. isi keranjang ada 2
        self.test_cart.addItem('Apel', 10000)
        self.test_cart.addItem('Anggur', 15000)

        # hapus 1 barang
        self.test_cart.deleteItem('Anggur')

        # test apakah isi chart == 1 setelah satu dihapus
        self.assertEqual(len(self.test_cart.cart),1, "Isi chart salah")
        
        # test apakah isi yang tersisa adalah Apel
        self.assertEqual(self.test_cart.cart[0].name, 'Apel')
       
        # test apakah ouput sesuai ketika menghapus barang yang tidak ada (karena sudah dihapus di atas) dalam keranjang
        self.assertEqual(self.test_cart.deleteItem('Anggur'), (f"\n>> Barang dengan kata 'Anggur' tidak ditemukan!"), 'Pesan yang ditampilkan tidak sesuai')
        
        # test apakah output sesuai ketika menghapus Apel
        self.assertEqual(self.test_cart.deleteItem('Apel'), (f"\n>> 'Apel' berhasil dihapus"), 'Pesan yang ditampilkan tidak sesuai')

        # test apakah isi chart sama dengan 0 ketika semua barang sudah dihapus
        self.assertEqual(len(self.test_cart.cart), 0, 'Isi chart salah')        
        
        # test apakah output sesuai ketika menghapus barang padahal isi chart kosong
        self.assertEqual(self.test_cart.deleteItem('Jeruk'), (f"\n>> Keranjang kosong, tidak menghapus apapun"))

    def test_totalPrice(self): 
        ''' 
        test untuk method totalPrice / menjumlahkan total harga belanjaan
        '''
        # tambahkan 2 barang terlebih dahulu
        self.test_cart.addItem('Apel', 10000)
        self.test_cart.addItem('Anggur', 15000)

        # test apakah total harga sama dengan harga apel dan anggur yang dijumlahkan
        self.assertEqual(self.test_cart.totalPrice(), 25000, "Hasil tidak sama")


if __name__ == "__main__":
    unittest.main()