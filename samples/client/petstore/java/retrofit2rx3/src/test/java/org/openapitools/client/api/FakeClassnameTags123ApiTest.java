package org.openapitools.client.api;

import org.openapitools.client.ApiClient;
import org.openapitools.client.model.Client;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FakeClassnameTags123Api
 */
public class FakeClassnameTags123ApiTest {

    private FakeClassnameTags123Api api;

    @BeforeEach
    public void setup() {
        api = new ApiClient().createService(FakeClassnameTags123Api.class);
    }

    /**
     * To test class name in snake case
     *
     * To test class name in snake case
     */
    @Test
    public void testClassnameTest() {
        Client body = null;
        // Client response = api.testClassname(body);

        // TODO: test validations
    }
}
