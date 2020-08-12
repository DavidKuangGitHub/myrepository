package softwaredefinedvehicle_v2;

public class Vehicle {
	private boolean ignition_on_off;
	String vehicleidentificationnumber;
	private int modelYear;

	public boolean isIgnition_on_off() {
		return ignition_on_off;
	}

	public void setIgnition_on_off(boolean ignition_on_off) {
		this.ignition_on_off = ignition_on_off;
	}

	public String getVIN() {
		return vehicleidentificationnumber;
	}

	public void setVIN(String regno) {
		this.vehicleidentificationnumber = regno;
	}

	public int getModelYear() {
		return modelYear;
	}

	public void setModelYear(int modelYear) {
		this.modelYear = modelYear;
	}

	public Vehicle() {
		ignition_on_off = false;
		vehicleidentificationnumber = "1FTYR44V03TA01830";/*
															 * 16 digit VIN number
															 */
		modelYear = 21;
	}

	public Vehicle(boolean ign_onoff, String r, int moye) {
		ignition_on_off = ign_onoff;
		vehicleidentificationnumber = r;
		modelYear = moye;
	}

	void display() {
		System.out.println("IgnitionStatus 		=	" + ignition_on_off);
		System.out.println("Registration Num	=	" + vehicleidentificationnumber);
		System.out.println("Model Year      	=	" + modelYear);
	}
}
