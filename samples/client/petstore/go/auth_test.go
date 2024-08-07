package main

import (
	"context"
	"net/http"
	"net/http/httputil"
	"strings"
	"testing"
	"time"

	"golang.org/x/oauth2"

	sw "github.com/OpenAPITools/openapi-generator/samples/client/petstore/go/go-petstore"
)

func TestOAuth2(t *testing.T) {
	// Setup some fake oauth2 configuration
	cfg := &oauth2.Config{
		ClientID:     "1234567",
		ClientSecret: "SuperSecret",
		Endpoint: oauth2.Endpoint{
			AuthURL:  "https://devnull",
			TokenURL: "https://devnull",
		},
		RedirectURL: "https://devnull",
	}

	// and a fake token
	tok := oauth2.Token{
		AccessToken:  "FAKE",
		RefreshToken: "So Fake",
		Expiry:       time.Now().Add(time.Hour * 100000),
		TokenType:    "Bearer",
	}

	// then a fake tokenSource
	tokenSource := cfg.TokenSource(createContext(nil), &tok)
	auth := context.WithValue(context.Background(), sw.ContextOAuth2, tokenSource)

	newPet := (sw.Pet{Id: sw.PtrInt64(12992), Name: "gopher",
		PhotoUrls: []string{"http://1.com", "http://2.com"}, Status: sw.PtrString("pending"),
		Tags: []sw.Tag{{Id: sw.PtrInt64(1), Name: sw.PtrString("tag2")}}})

	t.Log("Host is: ", client.GetConfig().Scheme+"://"+client.GetConfig().Host+", "+client.GetConfig().Servers[0].URL)

	r, err := client.PetAPI.AddPet(context.Background()).Body(newPet).Execute()

	if err != nil {
		t.Fatalf("Error while adding pet: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}

	r, err = client.PetAPI.DeletePet(auth, 12992).Execute()

	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}
	reqb, _ := httputil.DumpRequest(r.Request, true)

	if !strings.Contains((string)(reqb), "Authorization: Bearer FAKE") {
		t.Errorf("OAuth2 Authentication is missing")
	}
}

func TestAPIKeyNoPrefix(t *testing.T) {
	auth := context.WithValue(context.Background(), sw.ContextAPIKeys, map[string]sw.APIKey{"api_key": {Key: "TEST123"}})

	newPet := (sw.Pet{Id: sw.PtrInt64(12992), Name: "gopher",
		PhotoUrls: []string{"http://1.com", "http://2.com"}, Status: sw.PtrString("pending"),
		Tags: []sw.Tag{{Id: sw.PtrInt64(1), Name: sw.PtrString("tag2")}}})

	r, err := client.PetAPI.AddPet(context.Background()).Body(newPet).Execute()

	if err != nil {
		t.Fatalf("Error while adding pet: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}

	_, r, err = client.PetAPI.GetPetById(auth, 12992).Execute()
	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}

	reqb, _ := httputil.DumpRequest(r.Request, true)
	if !strings.Contains((string)(reqb), "api_key: TEST123") {
		t.Errorf("APIKey Authentication is missing")
	}

	r, err = client.PetAPI.DeletePet(auth, 12992).Execute()
	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}
}

func TestAPIKeyWithPrefix(t *testing.T) {
	auth := context.WithValue(context.Background(), sw.ContextAPIKeys, map[string]sw.APIKey{"api_key": {Key: "TEST123", Prefix: "Bearer"}})

	newPet := (sw.Pet{Id: sw.PtrInt64(12992), Name: "gopher",
		PhotoUrls: []string{"http://1.com", "http://2.com"}, Status: sw.PtrString("pending"),
		Tags: []sw.Tag{{Id: sw.PtrInt64(1), Name: sw.PtrString("tag2")}}})

	r, err := client.PetAPI.AddPet(nil).Body(newPet).Execute()

	if err != nil {
		t.Fatalf("Error while adding pet: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}

	_, r, err = client.PetAPI.GetPetById(auth, 12992).Execute()
	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}

	reqb, _ := httputil.DumpRequest(r.Request, true)
	if !strings.Contains((string)(reqb), "api_key: Bearer TEST123") {
		t.Errorf("APIKey Authentication is missing")
	}

	r, err = client.PetAPI.DeletePet(auth, 12992).Execute()
	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}
}

func TestDefaultHeader(t *testing.T) {
	newPet := (sw.Pet{Id: sw.PtrInt64(12992), Name: "gopher",
		PhotoUrls: []string{"http://1.com", "http://2.com"}, Status: sw.PtrString("pending"),
		Tags: []sw.Tag{{Id: sw.PtrInt64(1), Name: sw.PtrString("tag2")}}})

	r, err := client.PetAPI.AddPet(context.Background()).Body(newPet).Execute()

	if err != nil {
		t.Fatalf("Error while adding pet: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}

	r, err = client.PetAPI.DeletePet(context.Background(), 12992).Execute()

	if err != nil {
		t.Fatalf("Error while deleting pet by id: %v", err)
	}
	if r.StatusCode != 200 {
		t.Log(r)
	}
	reqb, _ := httputil.DumpRequest(r.Request, true)
	if !strings.Contains((string)(reqb), "Testheader: testvalue") {
		t.Errorf("Default Header is missing")
	}
}

func TestHostOverride(t *testing.T) {
	_, r, err := client.PetAPI.FindPetsByStatus(context.Background()).Status(nil).Execute()

	if err != nil {
		t.Fatalf("Error while finding pets by status: %v", err)
	}

	if r.Request.URL.Host != testHost {
		t.Errorf("Request Host is %v, expected %v", r.Request.Host, testHost)
	}
}

func TestSchemeOverride(t *testing.T) {
	_, r, err := client.PetAPI.FindPetsByStatus(context.Background()).Status(nil).Execute()

	if err != nil {
		t.Fatalf("Error while finding pets by status: %v", err)
	}

	if r.Request.URL.Scheme != testScheme {
		t.Errorf("Request Scheme is %v, expected %v", r.Request.URL.Scheme, testScheme)
	}
}

// Add custom clients to the context.
func createContext(httpClient *http.Client) context.Context {
	parent := oauth2.NoContext
	ctx := context.WithValue(parent, oauth2.HTTPClient, httpClient)
	return ctx
}
