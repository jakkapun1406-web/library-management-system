# ใน main.py
from book import Book
from library import Library

def show_menu():
    print("\n" + "="*50)
    print("🏛️  ระบบห้องสมุด")
    print("="*50)
    print("1. เพิ่มหนังสือ")
    print("2. แสดงหนังสือทั้งหมด")
    print("3. ค้นหาหนังสือ")
    print("4. ลบหนังสือ")
    print("5. ยืมหนังสือ")
    print("6. คืนหนังสือ")
    print("7. แสดงหนังสือที่ถูกยืม")
    print("8. ออกจากโปรแกรม")
    print("="*50)
def main():
    my_library = Library("ห้องสมุดประชาชน")

    # โหลดข้อมูลตอนเริ่มโปรแกรม
    print("📂 กำลังโหลดข้อมูล...")
    my_library.load_from_file()

    while True:
        show_menu()
        choice = input("เลือกเมนู (1-8): ")

        if choice == "1":
            # เพิ่มหนังสือ
            print("\n📚 เพิ่มหนังสือใหม่")
            title = input("ชื่อหนังสือ: ")
            author = input("ผู้แต่ง: ")
            isbn = input("ISBN: ")

            book = Book(title, author, isbn)
            my_library.add_book(book)

        elif choice == "2":
            # แสดงหนังสือทั้งหมด
            my_library.display_books()

        elif choice == "3":
            # ค้นหาหนังสือ
            title = input("\n🔍 ค้นหาหนังสือ: ")
            result = my_library.search_book(title)
            if result:
                print(f"✅ เจอ: {result}")
            else:
                print("❌ ไม่พบหนังสือที่ค้นหา")

        elif choice == "4":
            # ลบหนังสือ
            isbn = input("\n🗑️  ใส่ ISBN ที่จะลบ: ")
            my_library.remove_book(isbn)
        
        elif choice == "5":
            # ยืมหนังสือ
            isbn = input("\n📚 ใส่ ISBN หนังสือที่จะยืม: ")
            member_name = input("ชื่อผู้ยืม: ")
            my_library.borrow_book(isbn, member_name)
            
        elif choice == "6":
            # คืนหนังสือ
            isbn = input("\n📥 ใส่ ISBN หนังสือที่จะคืน: ")
            my_library.return_book(isbn)
        
        elif choice == "7": 
            #แสดงหนังสือที่ถูกยืม
            my_library.show_borrowed_books()  

        elif choice == "8":
            # ออกจากโปรแกรม
            print("\n💾 กำลังบันทึกข้อมูล...")
            my_library.save_to_file()
            print("👋 ขอบคุณที่ใช้บริการ!")
            break 

        else:
            print("❌ กรุณาเลือก 1-8 เท่านั้น")

        # รอให้ผู้ใช้กด Enter ก่อนแสดงเมนูใหม่
        input("\nกด Enter เพื่อดำเนินการต่อ...")


if __name__ == "__main__":
    main()