// TP-waterpark.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
using namespace std;
class customer
{
private:
    
};
class pool
{

};
class Food
{
private:
    int choice;
    int price;

public:
    void FoodChoice()//상호작용을 출력할 함수
    {
        cout << "원하는 장소를 고르세요" << endl;
        cout << "1.식당" << endl;
        cout << "2.매점" << endl;
        cout << "3.카페" << endl;
        cin >> choice;
        switch (choice)
            case 1:
        {
            cout << "원하는 상품의 가격을 입력하세요" << endl;
            cout << "1.곤드레돌솥비빔밥(15,000원)" << endl;
            cout << "2.돈까스(13500원)" << endl;
            cout << "3.크리스피치킨(22000원)" << endl;
            cin >> price;
            int Paycheck(customer & Cus);
            break;

            case 2:
                cout << "원하는 상품의 가격을 입력하세요" << endl;
                cout << "1.라면세트(10000원)" << endl;
                cout << "2.구운계란(3000원)" << endl;
                cout << "3.떡갈비 소세지(4000원)" << endl;
                cout << "4.탄산음료(2500원)" << endl;
                cin >> price;
                int Paycheck(customer & Cus);
                break;
            
            case 3:
                cout << "원하는 상품의 가격을 입력하세요" << endl;
                cout << "1.커피(4000원)" << endl;
                cout << "2.식혜(2500원)" << endl;
                cout << "3.아이스티(3000원)" << endl;
                cin >> price;
                int Paycheck(customer & Cus);
         }
    }
    int Paycheck(customer& Cus)
    {
        price += Cus.Account(~);  //함수명그냥임의로 Account라고 함.
        return price;
  
    }
};
class TicketOffice
{

};

int main()
{
    int choice;
    enum
    {
        TICKETOFFICE=1,POOL,RESTAURANT
    };
    cout << "키, 몸무게 튜브대여여부를 순서대로 입력해주세요" << endl;
    customer Cus;
    //cin>>cus.변수;//고객정보입력받기
   
    cout << "입장하셨습니다." << endl;
   
    while (1)
    {
        cout << "다음 장소를 고르세요.(단,퇴장하시려면 매표소로 가십시오)" << endl;
        cout << "1.매표소" << endl;
        cout << "2.수영장" << endl;
        cout << "3.식당" << endl;
        cin >> choice;
        switch (choice)
            case TICKETOFFICE:
                //상호작용출력하는함수(1.대여소,2.퇴장,3.매표소)
                //1.매표소->티켓안내->선택->가격정산
                //2.대여소->튜브,구명조끼안내->선택->가격정산
                //3.퇴장->가격정산출력->종료
                //break;
            case POOL:
                //int 함수명();
                //break;
            case RESTAURANT:
                void FoodChoice();
                break;

                return 0;
    }
}