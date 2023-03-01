package com.mistystrickland.displaydate.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController {

	@GetMapping("/")
	public String home() {
		return "I'm Coding!!!! YEAH!";
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
