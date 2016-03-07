/*
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 * 
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * @class
 * Initializes a new instance of the BaseProduct class.
 * @constructor
 * The product documentation.
 * @member {string} baseProductId Unique identifier representing a specific
 * product for a given latitude & longitude. For example, uberX in San
 * Francisco will have a different product_id than uberX in Los Angeles.
 * 
 * @member {string} [baseProductDescription] Description of product.
 * 
 */
function BaseProduct() {
}

/**
 * Defines the metadata of BaseProduct
 *
 * @returns {object} metadata of BaseProduct
 *
 */
BaseProduct.prototype.mapper = function () {
  return {
    required: false,
    serializedName: 'BaseProduct',
    type: {
      name: 'Composite',
      className: 'BaseProduct',
      modelProperties: {
        baseProductId: {
          required: true,
          serializedName: 'base_product_id',
          type: {
            name: 'String'
          }
        },
        baseProductDescription: {
          required: false,
          serializedName: 'base_product_description',
          type: {
            name: 'String'
          }
        }
      }
    }
  };
};

module.exports = BaseProduct;
