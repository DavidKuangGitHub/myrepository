package softwaredefinedvehicle_v2;

/*public class Threewheeler {

}*/
public class Threewheeler extends Vehicle {
	int noofwheel = 3;

	public Threewheeler() {
		super();
	}

	public Threewheeler(boolean threew_ignition_onoff, String threem_vin, int threew_modelyear, int n) {
		super();
		noofwheel = n;
	}

	public void display() {
		System.out.println("Three wheeler tvs");
		super.display();
		System.out.println("No. of wheel :" + noofwheel);
	}

}
