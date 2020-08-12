package testDK1JavaClasses;

import softwaredefinedvehicle_v2.Car;

public class testCar {

	public static void main(String[] args) {
		Car myCar = new Car();
		myCar.updateLicensePlateIfAny("BMAR601");
		System.out.println("The instanceofCar = " + myCar.getLicensePlate());
	}
}