package mypkg.crud;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/crud/")
public class CurdController {

    protected CrudService crudService;

    @Autowired
    public CurdController(CrudService crudService) {
        this.crudService = crudService;
    }

    @RequestMapping(method = RequestMethod.POST)
    public ResponseEntity<Person> create(@RequestBody Person person) {
        if (person == null) {
            return new ResponseEntity<>(HttpStatus.UNPROCESSABLE_ENTITY);
        }

        crudService.create(person.getName(), person.getAge());
        return new ResponseEntity<>(crudService.last(), HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.GET)
    public List<?> show() {
        return crudService.show();
    }

    @RequestMapping(value = "/{index}/", method = RequestMethod.GET)
    public Person get(@PathVariable("index") int index) {
        return crudService.get(index);
    }

    @RequestMapping(value = "/{index}/", method = RequestMethod.DELETE)
    public ResponseEntity<?> delete(@PathVariable("index") int index) {
        if (!crudService.delete(index)) {
            return new ResponseEntity<>("Out of index", HttpStatus.BAD_REQUEST);
        }
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @RequestMapping(value = "/{index}/", method = RequestMethod.PATCH)
    public ResponseEntity<?> patch(@PathVariable("index") int index, @RequestBody Person person) {
        crudService.patch(index, person);
        return new ResponseEntity<>(HttpStatus.OK);
    }

}
