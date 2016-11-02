import { EventEmitter } from '@angular/core';
import { ControlValueAccessor } from '@angular/forms';
export declare const RADIO_VALUE_ACCESSOR: any;
export declare class RadioButton implements ControlValueAccessor {
    value: any;
    name: string;
    disabled: boolean;
    label: string;
    onClick: EventEmitter<any>;
    model: any;
    onModelChange: Function;
    onModelTouched: Function;
    checked: boolean;
    hover: boolean;
    focused: boolean;
    handleClick(): void;
    select(): void;
    writeValue(model: any): void;
    registerOnChange(fn: Function): void;
    registerOnTouched(fn: Function): void;
    setDisabledState(val: boolean): void;
    onFocus(event: any): void;
    onBlur(event: any): void;
    onChange(event: any): void;
}
export declare class RadioButtonModule {
}
