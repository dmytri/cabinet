Feature: Verify dependencies in apply container

  @accept
  Scenario: Dependencies present in apply container
    When python >= 3.12
     And uv >= 0.6.7
     And pytest-bdd is required
     And poethepoet is required
     And httpx is required
     And kubernetes is required
