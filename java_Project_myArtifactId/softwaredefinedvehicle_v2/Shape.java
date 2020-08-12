package softwaredefinedvehicle_v2;

public abstract class Shape {
	Color color;
	
	void setColor(Color newColor) {
		color = newColor;
		redraw();
	}
	
	abstract void redraw();
	

}

class Color{}
