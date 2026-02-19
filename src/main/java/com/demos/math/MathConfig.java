package com.demos.math;

public class MathConfig {
    
    private boolean additionEnabled = true;
    private boolean subtractionEnabled = false;
    private boolean multiplicationEnabled = false;
    private boolean divisionEnabled = false;

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

    public boolean isMultiplicationEnabled() {
        return multiplicationEnabled;
    }

    public void setMultiplicationEnabled(boolean multiplicationEnabled) {
        this.multiplicationEnabled = multiplicationEnabled;
    }

    public boolean isDivisionEnabled() {
        return divisionEnabled;
    }

    public void setDivisionEnabled(boolean divisionEnabled) {
        this.divisionEnabled = divisionEnabled;
    }
}
