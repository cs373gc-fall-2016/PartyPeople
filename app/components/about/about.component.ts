import { Component } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
  selector: 'about',
  templateUrl: 'app/components/about/about.html',
  styleUrls: ['app/components/about/about.css'],
  providers: [
	AllServicesService
  ]
})
export class AboutComponent {
	private output = "";

	constructor(private allServicesService: AllServicesService) {}
	runUnitTests() {
		console.log("Running Unit Tests!");
		var div = document.getElementById('runTestsDiv');

		this.allServicesService.getTestOutput().subscribe(
			testOutput => {
				this.output = testOutput;
				div.innerHTML = this.output;
	    	});

		div.innerHTML = "Running Unit Tests!";
	}
}
