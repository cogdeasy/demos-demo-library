package com.demos.math;

public class MathConfig {
    
    private boolean additionEnabled = true;
    private boolean subtractionEnabled = false;

    public boolean isAdditionEnabled() {
        return additionEnabled;
    }

    public void setAdditionEnabled(boolean additionEnabled) {
        this.additionEnabled = additionEnabled;
    }

    public boolean isSubtractionEnabled() {
        return subtractionEnabled;
    }

    public void setSubtractionEnabled(boolean subtractionEnabled) {
        this.subtractionEnabled = subtractionEnabled;
    }
}
