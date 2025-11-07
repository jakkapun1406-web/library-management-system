# test_save.py
from book import Book
from library import Library

# สร้างห้องสมุด
my_library = Library("ห้องสมุดทดสอบ")

# เพิ่มหนังสือ 2 เล่ม
book1 = Book("Harry Potter", "J.K. Rowling", "12345")
book2 = Book("The Hobbit", "Tolkien", "67890")

my_library.add_book(book1)
my_library.add_book(book2)

# ทดสอบบันทึก
print("\n--- ทดสอบบันทึกข้อมูล ---")
my_library.save_to_file()

print("\n✅ ถ้าเห็นไฟล์ library_data.json แสดงว่าสำเร็จ!")