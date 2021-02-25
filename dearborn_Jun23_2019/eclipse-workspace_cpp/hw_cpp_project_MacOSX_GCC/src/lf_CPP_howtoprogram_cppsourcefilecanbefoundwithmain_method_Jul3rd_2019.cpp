#include <iostream>
#include <string>

using namespace std;

class GradeBook {

public:
	GradeBook(string constructorCN){
		setCourseName(constructorCN);
	}

	void setCourseName(string courseName){
		theCourseName=courseName;
	}
	string getCourseName(){
		return theCourseName;
	}
	void displayMessage(){
		cout<<"Welcome to the grade book for "<< getCourseName()<<"。"<<endl;
	}
private:
	string theCourseName;
};

int main(){
	GradeBook myGradeBook1("Code1 myGradeBook1");
	GradeBook myGradeBook2("Code2 myGradeBook2");


	myGradeBook1.displayMessage();
	cout<<"The name of Number1 is "<<myGradeBook1.getCourseName()<<endl;
	myGradeBook2.displayMessage();
	cout<<"The name of Number2 is "<<myGradeBook2.getCourseName()<<endl;

}

/*class GradeBook {

public:
	void setCourseName(string courseName){
		theCourseName=courseName;
	}
	string getCourseName(){
		return theCourseName;
	}
	void displayMessage(){
		cout<<"Welcome to the grade book for "<< getCourseName()<<" ."<<endl;
	}
private:
	string theCourseName;
};

int main_fig03_05again(){
	string nameOfCourse;
	GradeBook myGradeBook;
	cout<< "Please enter the course name: "<<endl;
	getline(cin, nameOfCourse);
	myGradeBook.setCourseName(nameOfCourse);
	myGradeBook.displayMessage();
}

class GradeBook {

public:
	void setCourseName(string courseName){
		theCourseName=courseName;
	}
	string getCourseName(){
		return theCourseName;
	}
	void displayMessage(){
		cout<<"This method of displayMessage is to show "<< getCourseName()<<" ."<<endl;
	}
private:
	string theCourseName;
};

int main_fig03_05(){
	string nameOfCourse;
	GradeBook myGradeBook;
	cout<< "In pre-setup, the initial course name is :"<< myGradeBook.getCourseName()<<endl;
	cout<< "Please enter the course name: "<<endl;
	getline(cin, nameOfCourse);
	myGradeBook.setCourseName(nameOfCourse);
	myGradeBook.displayMessage();
}

class GradeBook {
public:
	void displayMessage(string courseName) {
		cout << "This method of displayMessage is to display the name of "
				<< courseName << "!" << endl;
	}
};

int mainfig03_03() {
	GradeBook myGradeBook;
	string courseNameinMain;
	cout << "Please enter your course name: " << endl;
	getline(cin, courseNameinMain);
	cout << endl;

	myGradeBook.displayMessage(courseNameinMain);
}

class GradeBook_fig03_01 {
 public:
 void displayMessage(){
 cout<<"This method of displayMessage is to display the instance of this object."<<endl;
 }
 };

 int main_fig03_01(){
 GradeBook myGradeBook;
 myGradeBook.displayMessage();
 }*/

/*int main_fig02_13() {
 int number1, number2;

 cout << "Pls enter two integers to compare: ";
 cin >> number1 >> number2;

 if (number1 == number2)
 cout << number1 << " == " << number2 << endl;
 if (number1 != number2)
 cout << number1 << " != " << number2 << endl;
 if (number1 > number2)
 cout << number1 << " > " << number2 << endl;
 if (number1 < number2)
 cout << number1 << " < " << number2 << endl;
 if (number1 >= number2)
 cout << number1 << " >= " << number2 << endl;
 if (number1 <= number2)
 cout << number1 << " <= " << number2 << endl;

 }

 int main_fig02_05() {
 int number1;
 int number2;
 int sum;

 cout << "Please enter the first integer: ";
 cin >> number1;

 cout << "Please enter the second integer: ";
 cin >> number2;

 sum = number1 + number2;

 cout << "The Sum is " << sum << endl;

 }*/

