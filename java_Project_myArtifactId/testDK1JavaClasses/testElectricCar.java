package testDK1JavaClasses;

import softwaredefinedvehicle_v2.ElectricCar;

public class testElectricCar {

	public static void main(String[] args) {
		ElectricCar myElectricCar = new ElectricCar();
		myElectricCar.setModelname("Model 3");
		// myElectricCar.setManufacturename("Tesla");
		System.out.println("An instanceofElectricCar has Model = " + myElectricCar.getModelname() + " made by "
				+ myElectricCar.getManufacturename() + ".");
	}
	
}