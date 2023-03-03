package com.mistystrickland.displaydate.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

	@GetMapping("/")
	public String home() {
		return "home.jsp";
	}
	
	@GetMapping("/date")
	public String date() {
		return "Java! I Love You!";
	}
	
	@GetMapping("/time")
	public String time() {
		return "I Love CODING!!!!! Woo-Hoo!";
	}
}
