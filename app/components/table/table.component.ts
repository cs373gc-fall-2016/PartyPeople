import { Component } from '@angular/core';

@Component({
    selector: 'pp-table',
    templateUrl: 'app/components/table/table.html'
})
export class TableComponent {
	title = "fun fun fun";
	columns = ["NAME", "AGE", "COLOR"];
	data = [
		{"NAME": "julie", "AGE": "1", "COLOR": "blue"},
		{"NAME": "jack", "AGE": "2", "COLOR": "red"},
		{"NAME": "jane", "AGE": "3", "COLOR": "yellow"}
	];

}
