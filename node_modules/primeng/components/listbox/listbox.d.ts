import { ElementRef, EventEmitter, TemplateRef } from '@angular/core';
import { SelectItem } from '../common/api';
import { DomHandler } from '../dom/domhandler';
import { ControlValueAccessor } from '@angular/forms';
export declare const LISTBOX_VALUE_ACCESSOR: any;
export declare class Listbox implements ControlValueAccessor {
    el: ElementRef;
    domHandler: DomHandler;
    options: SelectItem[];
    multiple: boolean;
    style: any;
    styleClass: string;
    disabled: boolean;
    onChange: EventEmitter<any>;
    onDblClick: EventEmitter<any>;
    itemTemplate: TemplateRef<any>;
    value: any;
    onModelChange: Function;
    onModelTouched: Function;
    valueChanged: boolean;
    hoveredItem: any;
    constructor(el: ElementRef, domHandler: DomHandler);
    writeValue(value: any): void;
    registerOnChange(fn: Function): void;
    registerOnTouched(fn: Function): void;
    setDisabledState(val: boolean): void;
    onOptionClick(event: any, option: any): void;
    onOptionClickSingle(event: any, option: any): void;
    onOptionClickMultiple(event: any, option: any): void;
    isSelected(option: SelectItem): boolean;
    findIndex(option: SelectItem): number;
    onDoubleClick(event: Event, option: SelectItem): any;
}
export declare class ListboxModule {
}
