/*
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.openapitools.api;

import io.micronaut.http.annotation.*;
import io.micronaut.core.annotation.*;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.core.convert.format.Format;
import reactor.core.publisher.Mono;
import java.io.File;
import org.openapitools.model.ModelApiResponse;
import org.openapitools.model.Pet;
import java.util.Set;
import javax.annotation.Generated;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.validation.Valid;
import javax.validation.constraints.*;

@Generated(value="org.openapitools.codegen.languages.JavaMicronautClientCodegen", comments = "Generator version: 7.9.0-SNAPSHOT")
@Client("${petstore-micronaut-base-path}")
public interface PetApi {
    /**
     * Add a new pet to the store
     *
     * @param _body Pet object that needs to be added to the store (required)
     */
    @Post(uri="/pet")
    @Produces({"application/json", "application/xml"})
    Mono<Void> addPet(
        @Body @NotNull @Valid Pet _body
    );

    /**
     * Deletes a pet
     *
     * @param petId Pet id to delete (required)
     * @param apiKey  (optional)
     */
    @Delete(uri="/pet/{petId}")
    Mono<Void> deletePet(
        @PathVariable(name="petId") @NotNull Long petId, 
        @Header(name="api_key") @Nullable String apiKey
    );

    /**
     * Finds Pets by status
     * Multiple status values can be provided with comma separated strings
     *
     * @param status Status values that need to be considered for filter (required)
     * @return List&lt;Pet&gt;
     */
    @Get(uri="/pet/findByStatus")
    @Consumes({"application/xml", "application/json"})
    Mono<List<Pet>> findPetsByStatus(
        @QueryValue(value="status") @NotNull List<String> status
    );

    /**
     * Finds Pets by tags
     * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
     *
     * @param tags Tags to filter by (required)
     * @return Set&lt;Pet&gt;
     */
    @Get(uri="/pet/findByTags")
    @Consumes({"application/xml", "application/json"})
    Mono<Set<Pet>> findPetsByTags(
        @QueryValue(value="tags") @NotNull Set<String> tags
    );

    /**
     * Find pet by ID
     * Returns a single pet
     *
     * @param petId ID of pet to return (required)
     * @return Pet
     */
    @Get(uri="/pet/{petId}")
    @Consumes({"application/xml", "application/json"})
    Mono<Pet> getPetById(
        @PathVariable(name="petId") @NotNull Long petId
    );

    /**
     * Update an existing pet
     *
     * @param _body Pet object that needs to be added to the store (required)
     */
    @Put(uri="/pet")
    @Produces({"application/json", "application/xml"})
    Mono<Void> updatePet(
        @Body @NotNull @Valid Pet _body
    );

    /**
     * Updates a pet in the store with form data
     *
     * @param petId ID of pet that needs to be updated (required)
     * @param name Updated name of the pet (optional)
     * @param status Updated status of the pet (optional)
     */
    @Post(uri="/pet/{petId}")
    @Produces({"application/x-www-form-urlencoded"})
    Mono<Void> updatePetWithForm(
        @PathVariable(name="petId") @NotNull Long petId, 
        @Nullable String name, 
        @Nullable String status
    );

    /**
     * uploads an image
     *
     * @param petId ID of pet to update (required)
     * @param additionalMetadata Additional data to pass to server (optional)
     * @param _file file to upload (optional)
     * @return ModelApiResponse
     */
    @Post(uri="/pet/{petId}/uploadImage")
    @Consumes({"application/json"})
    @Produces({"multipart/form-data"})
    Mono<ModelApiResponse> uploadFile(
        @PathVariable(name="petId") @NotNull Long petId, 
        @Nullable String additionalMetadata, 
        @Nullable File _file
    );

    /**
     * uploads an image (required)
     *
     * @param petId ID of pet to update (required)
     * @param requiredFile file to upload (required)
     * @param additionalMetadata Additional data to pass to server (optional)
     * @return ModelApiResponse
     */
    @Post(uri="/fake/{petId}/uploadImageWithRequiredFile")
    @Consumes({"application/json"})
    @Produces({"multipart/form-data"})
    Mono<ModelApiResponse> uploadFileWithRequiredFile(
        @PathVariable(name="petId") @NotNull Long petId, 
        @NotNull File requiredFile, 
        @Nullable String additionalMetadata
    );

}
