package mypkg;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.model;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup;

import org.junit.Test;

import org.springframework.test.web.servlet.MockMvc;

public class WelcomeControllerTest {
	private WelcomeController controller = new WelcomeController();
	private MockMvc mockMvc = standaloneSetup(controller).build();

	@Test
	public void testHomePage() throws Exception {
		mockMvc.perform(get("/"))
                .andExpect(status().isOk())
                .andExpect(view().name("home"))
                .andExpect(model().attribute("name", "Spring MVC"));

		mockMvc.perform(get("/homepage")).andExpect(view().name("home"));
	}

	@Test
	public void testHiPage() throws Exception {
        String testName = "abc";
		mockMvc.perform(get("/hi?name=" + testName))
                .andExpect(status().isOk())
                .andExpect(view().name("home"))
                .andExpect(model().attribute("msg", "hi"))
                .andExpect(model().attribute("name", testName));
	}

    @Test
    public void testHelloPage() throws Exception {
        String testName = "xyz";
        mockMvc.perform(get("/hello/" + testName))
                .andExpect(status().isOk())
                .andExpect(view().name("home"))
                .andExpect(model().attribute("msg", "Hello"))
                .andExpect(model().attribute("name", testName));
    }
}
