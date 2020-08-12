package softwaredefinedvehicle_v2;

public class ElectricCar extends Car {

	String modelname;
	String manufacturename;

	public ElectricCar() {
		super();
		modelname = "Model S";
		manufacturename = "Tesla";
	}

	public ElectricCar(boolean evigntion_onoff, String ev_vin, int ev_modelyear, String ev_modelname,
			String ev_manname) {
		super();
		modelname = ev_modelname;
		manufacturename = ev_manname;
	}

	public void charge() {
		System.out.println("EV is been charging...");
	}

	public String getModelname() {
		return modelname;
	}

	public void setModelname(String modelname) {
		this.modelname = modelname;
	}

	public String getManufacturename() {
		return manufacturename;
	}

	public void setManufacturename(String manufacturename) {
		this.manufacturename = manufacturename;
	}
}