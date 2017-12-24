package mypkg.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/demo/")
public class DemoController {

    protected DemoService demoService;

    @Autowired
    public DemoController(DemoService demoService) {
        this.demoService = demoService;
    }

    @RequestMapping(value = "/hey/{name}/", method = RequestMethod.GET)
    @ResponseBody
    public String hey(@PathVariable("name") String name) {
        return demoService.hey(name);
    }

    @RequestMapping(value = "/hi/", method = RequestMethod.GET)
    @ResponseBody
    public String hi(@RequestParam("name") String name) {
        return demoService.hi(name);
    }
}
