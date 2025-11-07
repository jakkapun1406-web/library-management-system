# library.py
from datetime import datetime
import json

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
    def borrow_book(self, isbn,member_name):
        """ยืมหนังสือ"""
        for book in self.books:
            if getattr(book, "isbn", None) == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrowed_by = member_name  # เพิ่มข้อมูลผู้ยืม
                    book.borrowed_date = datetime.now()  # เพิ่มวันที่ยืม (ต้อง import datetime)
                    print(f"✅ {member_name} ยืม '{book.title}' สำเร็จ")
                    return True
                else:
                    # บอกว่าถูกใครยืมไปแล้ว
                    borrower = getattr(book, "borrowed_by", "ไม่ทราบ")
                    print(f"❌ หนังสือถูก {borrower} ยืมไปแล้ว")
                    return False
        print(f"❌ ไม่พบหนังสือ ISBN: {isbn}")
        return False
    def return_book(self, isbn):
        """คืนหนังสือ"""
        for book in self.books:
            if getattr(book, "isbn", None) == isbn:
                if book.is_borrowed:
                    borrowed_by = getattr(book, "borrowed_by", "ไม่ทราบ")
                    book.is_borrowed = False
                    book.borrowed_by = None  # ลบข้อมูลผู้ยืม
                    book.borrowed_date = None  # ลบวันที่ยืม
                    print(f"✅ {borrowed_by} คืน '{book.title}' สำเร็จ")
                    return True
                else:
                    print(f"❌ หนังสือนี้ไม่ได้ถูกยืม")
                    return False
        print(f"❌ ไม่พบหนังสือ ISBN: {isbn}")
        return False
    def show_borrowed_books(self):
        """แสดงหนังสือที่ถูกยืมทั้งหมด"""
        borrowed = [book for book in self.books if book.is_borrowed]
    
        if borrowed:
            print(f"\n📋 หนังสือที่ถูกยืม ({len(borrowed)} เล่ม):")
            print("="*60)
            for book in borrowed:
                borrower = getattr(book, "borrowed_by", "ไม่ทราบ")
                date = getattr(book, "borrowed_date", None)
                if date:
                    days = (datetime.now() - date).days
                    print(f"- {book.title} (ยืมโดย: {borrower}, {days} วันแล้ว)")
                else:
                    print(f"- {book.title} (ยืมโดย: {borrower})")
        else:
            print("\n✅ ไม่มีหนังสือที่ถูกยืม")
    
    def save_to_file(self,filename="library_data.json"):
        """บันทึกข้อมูลลงไฟล์ JSON"""
        
        # สร้างกล่องใส่ข้อมูล
        data = {
            "library_name":self.name, # ชื่อห้องสมุด (เช่น "ห้องสมุดประชาชน")
            "books":[]   # รายการหนังสือ (ตอนนี้ยังว่าง)

        }
        
        # วนลูปดูหนังสือทุกเล่ม
        for book in self.books:
            # สร้าง Dictionary สำหรับหนังสือแต่ละเล่ม
            book_data ={
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "is_borrowed": book.is_borrowed,
                "borrowed_by": book.borrowed_date.isoformat() if book.borrowed_date else None
            }
            # ใส่เข้ากล่อง
            data["books"].append(book_data)
    # บันทึกลงไฟล์

        try:
            with open(filename,'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ บันทึกข้อมูลสำเร็จ ({len(self.books)} เล่ม)")
            return True
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {e}")
            return False