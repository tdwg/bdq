var ConceptualFramework = function() {
	this.selectors = {};
	this.contextualized = {};
	this.selected = {};
	this.available = {};
	this.profile = {};		
	this.nD = 0;
	this.nE = 0;
}
ConceptualFramework.prototype.setupUseCase = function(selectorName,selectorDescription,selectorDefined) {							
	var self = this;
	self.profile["useCase"] = self.profile["useCase"]?self.profile["useCase"]:{};
	self.profile["useCase"].selectorName = $('#'+selectorName);
	self.profile["useCase"].selectorDescription = $('#'+selectorDescription);				
	self.profile["useCase"].selectorDefined = $('#'+selectorDefined);	
	var updateUseCase = function() {
		self.profile["useCase"].selectorDefined.html('<strong>'+self.profile["useCase"].selectorName.val()+'</strong>: '+self.profile["useCase"].selectorDescription.val());								
		self.profile["useCase"].name = self.profile["useCase"].selectorName.val();
		self.profile["useCase"].description = self.profile["useCase"].selectorDescription.val();
		self.updateProfile();
	}			
	self.profile["useCase"].selectorName.keyup(function() {
		updateUseCase();		
	});
	self.profile["useCase"].selectorDescription.keyup(function() {
		updateUseCase();		
	});	
}
ConceptualFramework.prototype.setupIE = function(selectorName,selectorDescription,selectorButton,selectorDefined) {							
	var self = this;
	self.available["ie"] = self.available["ie"]?self.available["ie"]:{};
	self.available["ie"].selectorName = $('#'+selectorName);
	self.available["ie"].selectorDescription = $('#'+ selectorDescription);
	self.available["ie"].selectorButton = $('#'+ selectorButton);
	self.available["ie"].selectorDefined = $('#'+ selectorDefined);		
	self.available["ie"].selectorButton.click(function() {	
		self.profile["ie"] = self.profile["ie"]?self.profile["ie"]:{};			
		self.profile["ie"][self.available["ie"].selectorName.val()] = self.available["ie"][self.available["ie"].selectorName.val()]?self.available["ie"][self.available["ie"].selectorName.val()]:{};
		self.profile["ie"][self.available["ie"].selectorName.val()].name  = self.available["ie"].selectorName.val();
		self.profile["ie"][self.available["ie"].selectorName.val()].description = self.available["ie"].selectorDescription.val();

		self.available["ie"].selectorDefined.append('<span><small><strong>'+self.profile["ie"][self.available["ie"].selectorName.val()].name+'</strong>: '+self.profile["ie"][self.available["ie"].selectorName.val()].description+'</small></span><br>');				
		self.contextualized["dimension"].selectorValuableIE.append('<option value="'+self.profile["ie"][self.available["ie"].selectorName.val()].name+'">'+self.profile["ie"][self.available["ie"].selectorName.val()].name+'</option>');		
		// self.updateProfileVIE();
		// Reveal.right();
		// Reveal.left();		
		self.available["ie"].selectorName.val('');
		self.available["ie"].selectorDescription.val('');
		self.updateProfile();
	});
}	
// ConceptualFramework.prototype.updateProfileUseCase = function() {
// 	var self = this;	
// 	$("h2[name*='profile_title'").html('DQ Profile for <strong>'+self.profile.useCase.value+'</strong>');				
// 	$("div[name*='profile_use_case_definition'").html('<strong>'+self.profile.useCase.value+' Use Case</strong> - '+self.profile.useCase.description+'');				
// }
// ConceptualFramework.prototype.updateProfileVIE = function() {
// 	var self = this;								
// 	$('#vie_content').html('');
// 	Object.keys(self.profile.ie).forEach(function(key) {
// 		$('#vie_content').append('<div style="width:90%;"><strong>'+self.profile.ie[key].value+'</strong> - '+self.profile.ie[key].description+'</div>');				
// 	});								
// }

ConceptualFramework.prototype.updateProfile = function() {
	var self = this;
	if(self.profile["useCase"] && self.profile["useCase"].name){		
		var content = '<strong>'+self.profile.useCase.name+':</strong> '+self.profile.useCase.description;
		$('#profile_use_case_definition').html(content);			
	}
	if(self.profile["ie"] && Object.keys(self.profile["ie"]).length>0){	
		$('#vie_content').html('');
		Object.keys(self.profile["ie"]).forEach(function(key) {
			var content = $('<div><strong>'+self.profile["ie"][key].name+':</strong> '+self.profile["ie"][key].description+'</div>');
			$('#vie_content').append(content);
		});		
	}
	if(self.profile["dimension"] && self.profile["dimension"].length>0){	
		$('#measurement_policy_content').html('');
		self.profile["dimension"].forEach(function(item) {
			var content = $('<div><strong>'+item.dimension.name+' of '+item.ie.name+' of '+item.resourceType+':</strong> '+item.definition+'</div>');
			$('#measurement_policy_content').append(content);
		});		
	}
	// if(self.profile["criterion"] && self.profile["criterion"].length>0){	
	// 	$('#measurement_policy_content').html('');
	// 	self.profile["criterion"].forEach(function(item) {
	// 		var content = $('<div><strong>'+item.criterion.name+' of '+item.ie.name+' of '+item.resourceType+':</strong> '+item.definition+'</div>');
	// 		$('#measurement_policy_content').append(content);
	// 	});		
	// }
}
// ConceptualFramework.prototype.updateMeasurementPolicy = function() {
// 	var self = this;								
// 	$('#measurement_policy_content').html('');
// 	Object.keys(self.profile.measurement).forEach(function(key) {
// 		console.log("LOG: ",self.profile.measurement[key].name);
// 		$('#measurement_policy_content').append('<div style="width:90%;"><strong>'+self.profile.measurement[key].name+'</strong> - '+self.profile.measurement[key].definition+'</div>');				
// 	});								
// }
// ConceptualFramework.prototype.updateValidationPolicy = function() {
// 	var self = this;								
// 	$('#validation_policy_content').html('');
// 	Object.keys(self.profile.validation).forEach(function(key) {
// 		$('#validation_policy_content').append('<div style="width:90%;">'+self.profile.validation[key].criterion+'</div>');				
// 	});								
// }
// ConceptualFramework.prototype.updateImprovementPolicy = function() {
// 	var self = this;								
// 	$('#improvement_policy_content').html('');
// 	Object.keys(self.profile.improvement).forEach(function(key) {
// 		$('#improvement_policy_content').append('<div style="width:90%;">'+self.profile.improvement[key].definition+' <strong>('+self.profile.improvement[key].dimension.resourceType.value+' - '+self.profile.improvement[key].enhancementType.value+')</strong></div>');				
// 	});								
// }
ConceptualFramework.prototype.updateContextualizedCriterion = function() {
	var self = this;
	self.selectors["criterion"].content.html('');	
	self.profile.dimension.forEach(function(currentDimension) {
		var content = $(`<div><strong>`+currentDimension.dimension.name+`</strong> of <strong>`+currentDimension.ie.name+`</strong> of <strong>`+currentDimension.resourceType+`</strong> must be: <input type="text"></input><br></div>`);	
		content.find('input').keyup(function() {
			self.profile["criterion"] = self.profile["criterion"]?self.profile["criterion"]:[];
			// self.profile["criterion"].push({name: currentDimension.dimension.name+' of '+currentDimension.ie.name+' of '+currentDimension.resourceType ' must be '+content.find('input').val()});
		});
		self.selectors["criterion"].content.append(content);
	});	
}
ConceptualFramework.prototype.setupContextualizedEnhancement = function(selectorContent) {									
	var self = this;
	self.selectors["enhancement"] = self.selectors["enhancement"]?self.selectors["enhancement"]:{};	
	self.selectors["enhancement"].content = $('#'+selectorContent);	
}			
ConceptualFramework.prototype.setupContextualizedCriterion = function(selectorContent) {									
	var self = this;
	self.selectors["criterion"] = self.selectors["criterion"]?self.selectors["criterion"]:{};
	self.selectors["criterion"].content = $('#'+selectorContent);			
}			
ConceptualFramework.prototype.setupContextualizedDimension = function(selectorAvailableDimensions,selectorValuableIE,selectorAvailableResourceType,selectorDimensionDefinition,selectorDimensionDescription,selectorDefinedDimension,dimensionButton) {									
	var self = this;
	self.contextualized["dimension"] = self.contextualized["dimension"]?self.contextualized["dimension"]:{};	
	self.contextualized["dimension"].selectorAvailableDimensions = $('#'+selectorAvailableDimensions);
	self.contextualized["dimension"].selectorValuableIE = $('#'+selectorValuableIE);
	self.contextualized["dimension"].selectorAvailableResourceType = $('#'+selectorAvailableResourceType);
	self.contextualized["dimension"].selectorDimensionDefinition = $('#'+selectorDimensionDefinition);	
	self.contextualized["dimension"].selectorDimensionDescription = $('#'+selectorDimensionDescription);	
	self.contextualized["dimension"].selectorDefinedDimension = $('#'+selectorDefinedDimension);	
	self.contextualized["dimension"].dimensionButton = $('#'+dimensionButton);		
	self.contextualized["dimension"].title = "DQ Dimensions";
	Object.keys(self.available["dimension"]).forEach(function(key) {
		var content = '<option value="'+key+'">'+self.available["dimension"][key].name+'</option>';
		self.contextualized["dimension"].selectorAvailableDimensions.append(content);
		self.contextualized["dimension"].selectorAvailableDimensions.change(function() {
			self.contextualized["dimension"].selectorDimensionDefinition.html('<small>'+self.available["dimension"][self.contextualized["dimension"].selectorAvailableDimensions.val()].description+'</small>');
		});
	});
	self.contextualized["dimension"].selectorDimensionDefinition.html('<small>'+self.available["dimension"][self.contextualized["dimension"].selectorAvailableDimensions.val()].description+'</small>');
	self.contextualized["dimension"].dimensionButton.click(function() {
		if(self.profile["ie"]){
			self.profile["dimension"] = self.profile["dimension"]?self.profile["dimension"]:[];
			self.profile["dimension"].push({
				dimension: self.available["dimension"][self.contextualized["dimension"].selectorAvailableDimensions.val()],
				ie: self.profile["ie"][self.contextualized["dimension"].selectorValuableIE.val()],
				resourceType: self.contextualized["dimension"].selectorAvailableResourceType.val(),
				definition: self.contextualized["dimension"].selectorDimensionDescription.val()
			});
			var content = `<strong>`+self.contextualized["dimension"].selectorAvailableDimensions.val()+`</strong> 
							of <strong>`+self.contextualized["dimension"].selectorValuableIE.val()+`</strong> 
							of <strong>`+self.contextualized["dimension"].selectorAvailableResourceType.val()+`: </strong>
							`+self.contextualized["dimension"].selectorDimensionDescription.val()+`<br>`;
			self.contextualized["dimension"].selectorDefinedDimension.append(content);
			self.updateContextualizedCriterion();
			self.updateContextualizedEnhancement();
			self.contextualized["dimension"].selectorDimensionDescription.val('');
			self.updateProfile();
		}
	});
}			
ConceptualFramework.prototype.addAvailableConcept = function(concept,id, value, description) {
	var	self = this;
	self.available[concept] = self.available[concept]?self.available[concept]:{};				
	self.available[concept][id] = {id:id, name:value,description:description};										
}			
ConceptualFramework.prototype.updateContextualizedEnhancement = function() {
	var self = this;
	if(self.profile["dimension"].length==1){
		self.selectors["enhancement"].content.html('');
		var select = $('<select></select>');
		self.profile.dimension.forEach(function(item) {
			var name = item.dimension.name + 'of ' + item.ie.name + ' of ' + item.resourceType;
			select.append('<option value="'+name+'">'+name+'</option>');
		});
		var content = $(`<div><input type="text" placeholder="What can be done... "></input> to improve </div>`).append(select);	
		self.selectors["enhancement"].content.append(content).append('<button>Add</button><br>');
	} else {
		self.selectors["enhancement"].content.find('select').html('');
		self.profile.dimension.forEach(function(item) {
			var name = item.dimension.name + 'of ' + item.ie.name + ' of ' + item.resourceType;
			self.selectors["enhancement"].content.find('select').append('<option value="'+name+'">'+name+'</option>');
		});
	}	
	self.selectors["enhancement"].content.find('button').click(function() {
		if(self.selectors["enhancement"].content.find('input').val().length>0){
			if(self.selectors["enhancement"].content.find('blockquote').length==0)self.selectors["enhancement"].content.append('<blockquote></blockquote>');
			var value = '<strong>'+self.selectors["enhancement"].content.find('input').val()+'</strong> to improve <strong>'+self.selectors["enhancement"].content.find('select').val()+'</strong><br>';
			self.selectors["enhancement"].content.find('blockquote').append(value);
			
			self.profile["enhancement"] = self.profile["enhancement"]?self.profile["enhancement"]:[];
			self.profile["enhancement"].name = value;

			self.selectors["enhancement"].content.find('input').val('');
			self.updateProfile();
		}		
	});
	// self.profile['enhancement'] = self.profile['enhancement']?self.profile['enhancement']:[];
	// self.profile['enhancement'].push({selector:content});		
	// var key = "enhancement";
	// if(Object.keys(self.profile.measurement).length==1) $("#"+self.contextualized[key].selectorId).html('');

	// Object.keys(self.profile.measurement).forEach(function(keyDimension) {	
	// 	var keyIE = self.profile.measurement[keyDimension].ie.id;				
	// 	if($('#content_'+key+'_'+keyIE+'_'+keyDimension).length==0){							
	// 		var content = $(`<section>
	// 			<h3 style="color: #eee8d5;">3. Define a set of important `+self.contextualized[key].title+` to improve <strong>`+self.profile.measurement[keyDimension].dimension.value+`</strong> of <strong>`+self.profile.ie[keyIE].value+`</strong> of <strong>`+self.profile.measurement[keyDimension].resourceType.value+`</strong></h3>	
	// 			<small>`+self.profile.measurement[keyDimension].definition+`</small>
	// 			<div id="content_enhancement_`+keyIE+'_'+keyDimension+`"></div>				
	// 			<blockquote id="`+key+`_`+keyIE+`_`+keyDimension+`_list">
	// 			</blockquote>
	// 			</section>`);
	// 		content.find('#content_'+key+'_'+keyIE+'_'+keyDimension).append('DQ Enhancement: <input id="input_'+key+'_'+keyIE+'_'+keyDimension+'" type="text"></input>');
	// 		var enhancementType = $('<select style="vertical-align: middle;" id="avaiable_enhancement_type_'+keyIE+'"></select>');
	// 		Object.keys(self.available.enhancementType).forEach(function(id) {
	// 			enhancementType.append('<option value="'+id+'">'+self.available.enhancementType[id].value+'</option>');	
	// 		});
	// 		var define = $('<button>Define</button>');
	// 		define.click(function() {
	// 			self.profile.improvement = self.profile.improvement?self.profile.improvement:{};
	// 			var enhancementTypeId = $('#avaiable_enhancement_type_'+keyIE).val();
	// 			var enhancementType = self.available.enhancementType[enhancementTypeId].value;				
	// 			var enhancementDefinition = $('#input_'+key+'_'+keyIE+'_'+keyDimension).val();											
	// 			var contextualizedId = enhancementTypeId+'-'+keyDimension+'-'+(self.nE++);
	// 			if(!self.profile.improvement[contextualizedId]){							
	// 				content.find('#'+key+'_'+keyIE+'_'+keyDimension+'_list').append(enhancementDefinition+' <strong>('+enhancementType+')</strong><br>');

	// 				self.profile.improvement[contextualizedId] = self.profile.improvement[contextualizedId]?self.profile.improvement[contextualizedId]:{};
	// 				self.profile.improvement[contextualizedId].dimension = self.profile.measurement[keyDimension];
	// 				self.profile.improvement[contextualizedId].ie = self.available.ie[keyIE];
	// 				self.profile.improvement[contextualizedId].enhancementType = self.available.enhancementType[enhancementTypeId];
	// 				self.profile.improvement[contextualizedId].definition = enhancementDefinition;					
	// 				self.updateImprovementPolicy();
	// 				Reveal.right();
	// 				Reveal.left();
	// 			}						
	// 		});
	// 		content.find("#content_"+key+"_"+keyIE+'_'+keyDimension).append("<br>").append("Enhancement Type: ").append(enhancementType).append("<br>").append(define);					
	// 		$("#"+self.contextualized[key].selectorId).append(content);	
	// 	}
	// });																	
}	

// ConceptualFramework.prototype.printAvailableConcept = function(concept) {
// 	var	self = this;
// 	Object.keys(self.available[concept]).forEach(function(key) {
// 		$("#"+self.selected[concept].selectorId).append('<option value="'+key+'">'+self.available[concept][key].value+'</option>');	
// 	});				
// }	