import { Component } from '@angular/core';

@Component({
  selector: 'about',
  templateUrl: 'app/components/about/about.html',
  styleUrls: ['app/components/about/about.css']
})
export class AboutComponent {
	
	runUnitTests() {
		console.log("Running Unit Tests!");
		var div = document.getElementById('runTestsDiv');
		div.innerHTML = "Running Unit Tests!";
	}
}
