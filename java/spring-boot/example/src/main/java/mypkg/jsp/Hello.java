package mypkg.jsp;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import java.util.HashMap;
import java.util.Map;


@Controller
@RequestMapping("/jsp/")
public class Hello {

    @RequestMapping("/hello/")
    public String hello(Model model, @RequestParam(value="name", required=false, defaultValue="Spring Boot + JSP") String name) {
        model.addAttribute("name", name);
        return "index";
    }

    @RequestMapping("/hi")
    public ModelAndView hi(@RequestParam(value="name", required=false, defaultValue="Spring Boot + JSP") String name) {
        ModelAndView modelAndView = new ModelAndView("index");
        modelAndView.addObject("name", name);
        return modelAndView;

//        return new ModelAndView("index", "name", name);
    }

}
