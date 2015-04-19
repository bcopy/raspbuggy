Blockly.Blocks['move'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(20);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["Move Forward for", "FORWARD"], ["Move Backwards for", "BACKWARDS"]]), "direction")
        .appendField(new Blockly.FieldTextInput("500"), "duration")
        .appendField("milliseconds");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};

Blockly.Blocks['turn'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.setColour(20);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["Turn left", "LEFT"], ["Turn right", "RIGHT"]]), "direction")
        .appendField("by")
        .appendField(new Blockly.FieldAngle("90"), "degrees")
        .appendField("degrees");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('');
  }
};
