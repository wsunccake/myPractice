package mypkg.demo;

import org.springframework.stereotype.Component;

@Component
public class DemoService {
    public String hi(String name) {
        return String.format("Hi %s", name);
    }

    public String hey(String name) {
        return String.format("Hey %s", name);
    }
}
