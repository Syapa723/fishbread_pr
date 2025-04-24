# develop branch

# 주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 제작예정
# input() 을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있음
stock = 0
class BreadShop :
    def __init__(self) :
        self.stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 8, "초코붕어빵" : 5}
        self.sales = {"팥붕어빵" : 0, "슈크림붕어빵" : 0, "초코붕어빵" : 0}
        self.price = {"팥붕어빵" : 1000, "슈크림붕어빵" : 1200, "초코붕어빵" : 1500}


# 붕어빵 주문
    def order_bread(self) :
        while True :
            bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 취소하려면 뒤로가기를 눌러주세요.")
            if bread_type == "뒤로가기" : 
                break
            if bread_type in self.stock :
                bread_count = int(input("주문할 붕어빵 수량을 입력하세요."))
                if  self.stock[bread_type] >= bread_count :
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f'{bread_type} {bread_count}개가 판매되었습니다.')
                else :
                    print(f'재고가 부족합니다. 현재 {self.stock[bread_type]}개만 주문가능합니다.')
            else :
                print('정신을 똑바로 차리시고 주문을 다시해주세요')

# 붕어빵 admin 기능
    def admin_mode(self):
        while True :
            bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 취소하려면 뒤로가기를 눌러주세요.")
            if bread_type == '뒤로가기':
                break
            if bread_type in stock :
                bread_count = int(input("창고에 채워넣을 붕어빵 수량을 입력하세요:"))
                self.stock[bread_type] += bread_count
                print(f'{bread_type}의 재고가 {bread_count}개 추가되어, {stock[bread_type]}개 입니다.')
            else :
                print('정신을 똑바로 차리시고 주문을 다시해주세요')
            
    def calculate_sales(self) : 
        #total_sales = (sales[key] * price[key] for key in sales) 
        total = 0
        for key in self.sales :
            total += (self.sales[key] * self.price[key])
        print(f'오늘의 총 매출은 {total}원 입니다.')
            