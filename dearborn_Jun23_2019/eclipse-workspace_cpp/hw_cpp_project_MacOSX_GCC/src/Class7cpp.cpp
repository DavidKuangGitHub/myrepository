#include <iostream>
#include <string>
#include "Class7cpp.h"

namespace std {

Class7_cpp::Class7_cpp(string name) {
	setCourseName(name);

}
void Class7_cpp::setCourseName(string name) {
	if (name.length() <= 25)
		courseName = name;
	if (name.length() > 25) {
		courseName = name.substr(0, 25);
		cout << "Your name <<" << name
				<< ">> exceeds maximum length (25).\n Limiting the first 25 characters.\n"
				<< endl;

	}
}
string Class7_cpp::getCourseName() {
	return courseName;
}
void Class7_cpp::displayMessage() {
	cout << "Welcome to the grade book for <<" << getCourseName() << ">>"
			<< endl;
}

Class7_cpp::~Class7_cpp() {
}

} /* namespace std */
