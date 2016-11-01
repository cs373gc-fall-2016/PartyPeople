"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var router_1 = require('@angular/router');
var StateDetailsComponent = (function () {
    function StateDetailsComponent(route) {
        this.route = route;
        this.stateName = "Texas";
        this.columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
        this.data = { "STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps" };
    }
    StateDetailsComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.sub = this.route.params.subscribe(function (params) {
            _this.id = +params['id'];
            // In a real app: dispatch action to load the details here.
        });
    };
    StateDetailsComponent.prototype.ngOnDestroy = function () {
        this.sub.unsubscribe();
    };
    StateDetailsComponent = __decorate([
        core_1.Component({
            selector: 'state-details',
            templateUrl: 'app/components/state_details/state_details.html',
        }), 
        __metadata('design:paramtypes', [router_1.ActivatedRoute])
    ], StateDetailsComponent);
    return StateDetailsComponent;
}());
exports.StateDetailsComponent = StateDetailsComponent;
//# sourceMappingURL=state_details.component.js.map