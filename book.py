# book.py
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False 
        self.borrowed_by = None      # เพิ่มบรรทัดนี้
        self.borrowed_date = None   # เพิ่มบรรทัดนี้
    
    def __str__(self):
        status = "ถูกยืมแล้ว" if self.is_borrowed else "พร้อมให้ยืม"
        
        # ถ้ามีข้อมูลผู้ยืม
        if self.is_borrowed and hasattr(self, "borrowed_by") and self.borrowed_by:
            return f"'{self.title}' โดย {self.author} (ISBN: {self.isbn}) - ยืมโดย: {self.borrowed_by}"
        else:
            return f"'{self.title}' โดย {self.author} (ISBN: {self.isbn}) - {status}"