from fishbread_model import BreadShop

shop = BreadShop()

while True :
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    # mode = 종료
    if mode == "종료" :
        shop.calculate_sales()
        print("시스템을 종료합니다.")
        break
    elif mode == "주문" :
        shop.order_bread()
    elif mode == "관리자" :
        shop.admin_mode()
    print("시스템이 종료 되었습니다.")

    # 로직이 숨겨지고 / 로직만 별도로 관리하기에 유지 보수가 쉬워짐