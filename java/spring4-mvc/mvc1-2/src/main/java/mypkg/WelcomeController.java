package mypkg;

import org.springframework.stereotype.Controller;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import java.util.Map;

@Controller
@RequestMapping(value = {"/", "/homepage"})
public class WelcomeController {

	@RequestMapping(method = RequestMethod.GET)
	public String home(Map<String, Object> model) {
		model.put("msg", "This is");
		model.put("name", "Spring MVC");
		return "home";
	}

	@RequestMapping(value = "/hi", method = RequestMethod.GET)
	public ModelAndView requestParamName(@RequestParam("name") String name) {
		ModelAndView model = new ModelAndView();
		model.setViewName("home");
		model.addObject("msg", "hi");
		model.addObject("name", name);
		return model;
	}

	@RequestMapping(value = "/hello/{name:.+}", method = RequestMethod.GET)
	public String pathVariableName(@PathVariable("name") String name, Map<String, Object> model) {
		model.put("msg", "Hello");
		model.put("name", name);
		return "home";
	}



}
