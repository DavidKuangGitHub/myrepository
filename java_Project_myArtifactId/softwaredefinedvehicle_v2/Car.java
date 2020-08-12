package softwaredefinedvehicle_v2;

public class Car extends Vehicle {

	protected String licensePlateIfAny = null;

	@Override
	public String getVIN() {
		return vehicleidentificationnumber;
	}

	@Override
	public void setVIN(String carVin) {
		super.setVIN(carVin);
	}

	public String getLicensePlate() {
		return licensePlateIfAny;
	}

	public void updateLicensePlateIfAny(String carlicense) {
		this.licensePlateIfAny = carlicense;
	}
}