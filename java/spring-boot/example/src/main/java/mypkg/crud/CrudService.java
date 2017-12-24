package mypkg.crud;

import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public class CrudService {

    private List<Person> people = new ArrayList<>();

    public Person create(String name, int age) {
        Person person = new Person();
        person.setName(name);
        person.setAge(age);
        people.add(person);
        return person;
    }

    public List<Person> show() {
        return people;
    }

    public Person get(int index) {
        if (index > people.size()) {
            return new Person();
        }

        return people.get(index);
    }

    public Person last() {
        return people.get(people.size() - 1);
    }

    public boolean delete(int index) {
        people.remove(index);
        return true;
    }

    public boolean patch(int index, Person person) {
        Person p = people.get(index);
        p.setName(person.getName());
        p.setAge(person.getAge());
        return true;
    }
}
