Blockly.Python['mov_move'] = function(block) {
  var value_direction = Blockly.Python.valueToCode(block, 'direction', Blockly.Python.ORDER_ATOMIC);
  var dropdown_direction = block.getFieldValue('direction');
  var value_duration = Blockly.Python.valueToCode(block, 'duration', Blockly.Python.ORDER_ATOMIC);
  var text_seconds = block.getFieldValue('seconds');
  // TODO: Assemble Python into code variable.
  var code = 'raspbuggy.move("'+value_direction+'",'+dropdown_direction+','+text_seconds+')\n';
  return code;
};

Blockly.Python['mov_turn'] = function(block) {
  var dropdown_direction = block.getFieldValue('direction');
  var angle_degrees = block.getFieldValue('degrees');
  // TODO: Assemble JavaScript into code variable.
  var code = 'raspbuggy.turn("'+dropdown_direction+'",'+angle_degrees+')\n';
  return code;
};

Blockly.Python['mov_rotate'] = function(block) {
  var dropdown_wheels = block.getFieldValue('wheels');
  var dropdown_direction = block.getFieldValue('direction');
  var dropdown_speed = block.getFieldValue('speed');
  // TODO: Assemble Python into code variable.
  var code = 'raspbuggy.rotate("'+dropdown_wheels+'","'+dropdown_direction+'","'+dropdown_speed+'")\n';
  return code;
};

Blockly.Python['mov_stop'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'raspbuggy.stop()\n';
  return code;
};

Blockly.Python['vis_acquire'] = function(block) {
  var dropdown_resolution = block.getFieldValue('resolution');
  // TODO: Assemble Python into code variable.
  var code = '# Call Vision acquiry function\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['vis_shapes'] = function(block) {
  var value_picture_input = Blockly.Python.valueToCode(block, 'picture_input', Blockly.Python.ORDER_ATOMIC);
  var dropdown_shape = block.getFieldValue('shape');
  // TODO: Assemble Python into code variable.
  var code = '# Call Vision shape comparison function';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Python['vis_filter'] = function(block) {
  var value_picture_input = Blockly.Python.valueToCode(block, 'picture_input', Blockly.Python.ORDER_ATOMIC);
  var dropdown_filter = block.getFieldValue('filter');
  // TODO: Assemble Python into code variable.
  var code = '# Call Vision filter function\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['sen_obstacle_distance'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '# Call Obstacle distance function\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['sen_obstacle_presence'] = function(block) {
  var dropdown_direction = block.getFieldValue('direction');
  var text_distancecm = block.getFieldValue('distanceCm');
  // TODO: Assemble Python into code variable.
  var code = '# Call Obstacle presence function\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['time_wait'] = function(block) {
  var text_waitinms = block.getFieldValue('waitInMs');
  var code = 'time.sleep('+(text_waitinms/1000)+')';
  return code;
};
