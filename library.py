# library.py
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # เก็บหนังสือทั้งหมด
    
    def add_book(self, book):
        """เพิ่มหนังสือเข้าห้องสมุด"""
        # TODO: เขียนโค้ดตรงนี้
        self.books.append(book)
        print(f"เพิ่มหนังสือสำเร็จ :{book}")
    
    def display_books(self):
        """แสดงหนังสือทั้งหมด"""
        # TODO: เขียนโค้ดตรงนี้
        print(f"รายการหนังสือในห้องสมุด {self.name}:")
        if self.books :#ตรวจสอบว่ามีหนังสือหรือไม่
            for book in self.books:
                print(f"-{book}")
        else:
            print("ไม่มีหนังสือในห้องสมุดขณะนี้")
    def search_book(self, title):
        """ค้นหาหนังสือจากชื่อ"""
        # TODO: เขียนโค้ดตรงนี้
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None #ถ้าไม่เจอ
    
    def remove_book(self, isbn):
        """ลบหนังสือจาก ISBN"""
        # TODO: เขียนโค้ดตรงนี้
        for book in self.books:
            if getattr(book, "isbn", None) == isbn:
                self.books.remove(book)
                print(f"ลบหนังสือสำเร็จ :{book}")
                return True
        print(f"ไม่พบหนังสือที่มี ISBN: {isbn}")
        return False
#ยืมหนังสือ
def borrow_book(self, isbn):
    """ยืมหนังสือ"""
    for book in self.books:
        if getattr(book, "isbn", None) == isbn:
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"✅ ยืมหนังสือสำเร็จ: {book}")
                return True
            else:
                print(f"❌ หนังสือถูกยืมไปแล้ว")
                return False
    print(f"❌ ไม่พบหนังสือที่มี ISBN: {isbn}")
    return False

def return_book(self, isbn):
    """คืนหนังสือ"""
    for book in self.books:
        if getattr(book, "isbn", None) == isbn:
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"✅ คืนหนังสือสำเร็จ: {book}")
                return True
            else:
                print(f"❌ หนังสือนี้ไม่ได้ถูกยืม")
                return False
    print(f"❌ ไม่พบหนังสือที่มี ISBN: {isbn}")
    return False

