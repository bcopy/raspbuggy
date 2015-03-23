package org.github.raspbuggy.jersey;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(namespace = "org.github.blockars.jersey")
public class Health {

    private String status;

    protected Health() {
    }

    public Health(String status) {
        this.status = status;
    }

    public String getStatus() {
        return status;
    }
}
