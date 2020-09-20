#include <iostream>
using namespace std;
/*
#define ID_LEN 20;
#define MAX_SPD 200;
#define FUEL_STEP 2;
#define ACC_STEP 10;
#define BRK_STEP 10;

struct Car
{
	char gamerID[ID_LEN];
	int fuelGauge;
	int curSpeed;
};

void ShowCarState(const Car& car)
{
	cout << "소유자 ID: " << car.gamerID << endl;
	cout << "연료량: " << car.fuelGauge <<"%"<< endl;
	cout << "현재속도: " << car curSpeed <<"km/s"<< endl<<endl;

}
void Accel(Car& car)
{
	if (car.fuelGauge <= 0)
		return;
	else
		car.fuelGauge -= FUEL_STEP;

	if (car.curSpeed + ACC_STEP >= MAX_SPD)
	{
		car.curSpeed = MAX_SPD;
		return;
	}

	car.curSpeed += ACC_STEP;
}
void Break(Car& car)
{
	if (car.curSpeed < BRK_STEP)
	{
		car.curSpeed = 0;
		return;
	}

	car.curSpeed -= BRK_STEP;
}

int main(void)
{
	Car run99 = { "run99",100,0 };
	Accel(run99);
	Accel(run99);
	ShowCarState(run99);
	Break(run99);
	ShowCarState(run99);

	Car sped77 = { "sped77",100,0 };
	Accel(sped77);
	Break(sped77);
	ShowCarState(sped77);
	return 0;

}


namespace CAR_CONST
{
	enum
	{
		ID_LEN = 20,
		MAX_SPD =200,
		FUEL_STEP=2,
		ACC_STEP=10,
		BRK_STEP=10
	};
}

struct Car
{
	char gamerID[CAR_CONST::ID_LEN];
	int fuelGuage;
	int curSpeed;

	void ShowCarState()
	{
		cout << "소유자ID: " << gamerID << endl;
		cout << "연료량: " << fuelGauge << "%" << endl;
		cout << "현재속도: " << curSpeed << "km/s" << endl << endl;
	}
	void Accel()
	{
		if (fuelGauge <= 0)
			return;
		else
			fuelGauge -= CAR_CONST::FUEL_STEP;

		if ((cuSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD)
		{
			curSpeed = CAT_CONST::MAX_SPD;
			return;
		}
		curSpeed += CAR_CONST::ACC_STEP;
	}
	void Break()
	{
		if (curSpeed < CAR_CONST::BRK_STEP)
		{
			curSpeed = 0;
			return;
		}
		curSpeed -= CAR_CONST::BRK_STEP;
	}

};

int main(void)
{
	Car run99 = { "run99",100,0 };
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	Car sped77 = { "sped77",100,0 };
	sped77.Accel();
	sped77.Break();
	sped77.ShowCarState();
	return 0;
}

namespace CAR_CONST
{
	enum
	{
		ID_LEN = 20,
		MAX_SPD = 200,
		FUEL_STEP = 2,
		ACC_STEP = 10,
		BRK_STEP = 10
	};
}

struct Car
{
	char gamerID[CAR_CONST::ID_LEN];
	int fuelGauge;
	int curSpeed;

	void ShowCarState();
	void Accel();
	void Break();

};

void Car::ShowCarState()
{
	cout << "소유자ID: " << gamerID << endl;
	cout << "연료량: " << "%" << endl;
	cout << "현재속도:" << "km/s" << endl << endl;
}
void Car::Accel()
{
	if (fuelGauge <= 0)
		return;
	else
		fuelGauge -= CAR_CONST::FUEL_STEP;

	if ((curSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD)
	{
		curSpeed = CAR_CONST::MAX_SPD;
		return;
	}

	curSpeed += CAR_CONST::ACC_STEP;
}

void Car::Break()
{
	if (curSpeed < CAR_CONST::BRK_STEP)
	{
		curSpeed = 0;
		return;
	}

	curSpeed -= CAR_CONST::BRK_STEP;
}

int main(void)
{
	Car run99 = { "run99",100,0 };
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();
	return 0;
}


#include <cstring>

namespace CAR_CONST
{
	enum
	{
		ID_LEN=20, MAX_SPD=200, FUEL_STEP=2,
		ACC_STEP=10,BRK_STEP=10
	};
}

class Car
{
private:
	char gamerID[CAR_CONST::ID_LEN];
	int fuelGauge;
	int curSpeed;
public:
	void InitMembers(char* ID, int fuel); //새로운 함수등장
	void ShowCarState();
	void Accel();
	void Break();
};

void Car::InitMembers(char* ID, int fuel)
{
	strcpy(gamerID, ID);
	fuelGuage = fuel;
	curSpeed = 0;
}
void Car::ShowCarState()
{
	cout << "소유자ID: " << gamerID << endl;
	cout << "연료량: " << fuelGauge << "%" << endl;
	cout << "현재속도: " << curSpeed << "km/s" << endl << endl;
}

void Car::Accel()
{
	if (fuelGauge <= 0)
		return;
	else
		fuelGauge -= CAR_CONST::FUEL_STEP;

	if ((curSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD)
	{
		curSpeed = CAR_CONST::MAX_SPD;
		return;
	}
	curSpeed += CAR_CONST::ACC_STEP;
}
void Car::Break()
{
	if (curSpeed < CAR_CONST::BRK_STEP)
	{
		curSpeed = 0;
		return;
	}
	curSpeed -= CAR_CONST::BRK_STEP;
}

int main(void)
{
	Car run99;
	run99.InitMembers("run99", 100);
	run99.Accel();
	run99.Accel();
	run99.Accel(); 
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();
	return 0;

}
*/
/*
class FruitSeller
{
private:
	int APPLE_PRICE;
	int numOfApples;
	int myMoney;

public:
	void InitMembers(int price, int num, int money)
	{
		APPLE_PRICE = price;
		numOfApples = num;
		myMoney = money;
	}
	int  SaleApples(int money)
	{
		int num = money / APPLE_PRICE;
		numOfApples = num;
		myMoney = money;
		return num;
	}
	void ShowSalesResult()
	{
		cout << "남은 사과: " << numOfApples << endl;
		cout << "판매수익: " << myMoney << endl;
	}
};

class FruitBuyer
{
	int myMoney;
	int numOfApples;
public:
	void InitMembers(int money)
	{
		myMoney = money;
		numOfApples = 0;
	}
	void BuyApples(FruitSeller & seller, int money)
	{
		numOfApples += seller.SaleApples(money);
		myMoney -= money;
	}
	void ShowBuyResult()
	{
		cout << "현재 잔액: " << myMoney << endl;
		cout << "사과 개수: " << numOfApples << endl << endl;
	}
};

int main(void)
{
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	buyer.BuyApples(seller, 2000);

	cout << "과일판매자의 현황" << endl;
	seller.ShowSalesResult();
	cout << "과일구매자의 현황" << endl;
	buyer.ShowBuyResult();
	return 0;
}*/

/*
FruitSeller,FruitBuyer클래스를작성하시오.
판매자와 구매자의 현황이 나오도록. 현재잔액과 사과개수가 나오도록.
int main(void)
{
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	buyer.BuyApples(seller, 2000);

	cout << "과일판매자의 현황" << endl;
	seller.ShowSalesResult();
	cout << "과일구매자의 현황" << endl;
	buyer.ShowBuyResult();
	return 0;
}
메인함수는 위와 같음.

*/

class FruitSeller
{
private:
	int numApples;  //사과개수
	int myMoney;   //my잔액
	int APPLE_PRICE;  //사과금액
public:
	void InitMembers(int Appleprice, int num, int money);  //매개변수선언잊지않기
	void ShowSalesResult();   //판매자현황출력
	void SellApples(FruitSeller& seller, int  money);   //사과판매실행
};

void FruitSeller::InitMembers(int Appleprice, int num, int money)
{
	FruitSeller::numApples = num;
	FruitSeller::myMoney = money;
	FruitSeller::APPLE_PRICE = Appleprice;
};

void FruitSeller::ShowSalesResult()
{
	cout << "현재 잔액: " << myMoney << endl;
	cout << "현재 사과 개수: " << numApples << endl;
}
void FruitSeller::SellApples(FruitSeller & seller,int  money)  
{
	
	seller.myMoney += money;   //판매자잔액
	seller.numApples -= money / APPLE_PRICE;   //판매자의 사과개수
}

class FruitBuyer
{
private:
	int numApples;
	int myMoney;
	int APPLE_PRICE;
public:
	void InitMembers(int money);
	void ShowBuyResult();
	void BuyApples(FruitBuyer& buyer, int money);
};

void FruitBuyer::InitMembers(int money)
{
	myMoney = money;

};

void FruitBuyer::ShowBuyResult()
{
	cout << "현재 구매자 잔액: " << myMoney << endl;
	cout << "현재 구매자가 가진 사과 개수: " << numApples << endl;
};

void FruitBuyer::BuyApples(FruitBuyer& buyer, int money)
{

	numApples += money / APPLE_PRICE;
	myMoney -= money;
};

int main(void)
{
	FruitSeller seller;
	seller.InitMembers(1000, 20, 0);
	FruitBuyer buyer;
	buyer.InitMembers(5000);
	buyer.BuyApples(buyer, 2000);

	cout << "과일판매자의 현황" << endl;
	seller.ShowSalesResult();
	cout << "과일구매자의 현황" << endl;
	buyer.ShowBuyResult();
	return 0;
}