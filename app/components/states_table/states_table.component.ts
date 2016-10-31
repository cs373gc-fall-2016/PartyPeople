import { Component } from '@angular/core';

@Component({
    selector: 'states-table',
    templateUrl: 'app/components/states_table/states_table.html'
})
export class StatesTableComponent {
	title = "State";
	columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
	data = [
		{"STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps"},
		{"STATE NAME": "Colorado", "CAPITAL": "Denver", "POPULATION": "987654", "GOVERNOR": "asdfeqwrasdf", "PARTY IN CONTROL": "dems"},
		{"STATE NAME": "Arizona", "CAPITAL": "Phoenix", "POPULATION": "325478951", "GOVERNOR": "someone", "PARTY IN CONTROL": "who knows"}
	];

}
