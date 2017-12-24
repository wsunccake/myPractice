package mypkg;

import static org.assertj.core.api.Assertions.assertThat;
import static org.hamcrest.Matchers.containsString;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import mypkg.demo.DemoController;
import mypkg.demo.DemoService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class MyAppTest {

    @Autowired
    private DemoController demoController;

    @Test
    public void contextLoads() throws Exception {
        assertThat(demoController).isNotNull();
    }


    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private DemoService demoService;

    @Test
    public void greetingShouldReturnMessageFromService() throws Exception {
        when(demoService.hi("SpringBoot")).thenReturn("Hi SpringBoot");
        this.mockMvc.perform(get("/hi?name=SpringBoot")).andDo(print()).andExpect(status().isOk())
                .andExpect(content().string(containsString("Hi SpringBoot")));
    }
}
