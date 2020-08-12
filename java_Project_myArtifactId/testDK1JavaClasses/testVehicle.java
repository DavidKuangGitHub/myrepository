package testDK1JavaClasses;

import softwaredefinedvehicle_v2.Vehicle;

public class testVihicle {

	public static void main(String[] args) {
		Vehicle myVehicle = new Vehicle();
		System.out.println("The instanceofVehicle = " + myVehicle.getVIN());
		System.out.println("The instanceofVehicle = " + myVehicle.isIgnition_on_off());
	}
}
