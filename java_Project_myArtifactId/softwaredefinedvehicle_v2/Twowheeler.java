package softwaredefinedvehicle_v2;

public class Twowheeler extends Vehicle {
	int noofwheel = 2;

	public Twowheeler() {
		super();
	}

	public Twowheeler(boolean twow_ignition_onoff, String twom_vin, int twow_modelyear, int n) {
		super();
		noofwheel = n;
	}

	public void display() {
		System.out.println("Two wheeler tvs");
		super.display();
		System.out.println("No. of wheel :" + noofwheel);
	}

}
