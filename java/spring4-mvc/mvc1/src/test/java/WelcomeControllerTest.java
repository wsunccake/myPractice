package mypkg;

import static org.junit.Assert.assertEquals;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup;

import org.junit.Test;

//import mypkg.WelcomeController;
import org.springframework.test.web.servlet.MockMvc;

public class WelcomeControllerTest {
	@Test
	public void testHomePage() throws Exception {
		WelcomeController controller = new WelcomeController();
		assertEquals("home", controller.home());

		MockMvc mockMvc = standaloneSetup(controller).build();
		mockMvc.perform(get("/")).andExpect(view().name("home"));

	}
}
