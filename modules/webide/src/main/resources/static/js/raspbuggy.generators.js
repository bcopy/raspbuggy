Blockly.Python['move'] = function(block) {
  var value_direction = Blockly.Python.valueToCode(block, 'direction', Blockly.Python.ORDER_ATOMIC);
  var dropdown_direction = block.getFieldValue('direction');
  var value_duration = Blockly.Python.valueToCode(block, 'duration', Blockly.Python.ORDER_ATOMIC);
  var text_seconds = block.getFieldValue('seconds');
  // TODO: Assemble Python into code variable.
  var code = '# call the move method';
  return code;
};

Blockly.JavaScript['turn'] = function(block) {
  var dropdown_direction = block.getFieldValue('direction');
  var angle_degrees = block.getFieldValue('degrees');
  // TODO: Assemble JavaScript into code variable.
  var code = '...';
  return code;
};
